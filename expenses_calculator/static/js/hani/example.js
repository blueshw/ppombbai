//{% load staticfiles %}
//var data = [
//	{author: "peter", text:"1번 댓글"},
//	{author: "bono", text:"1123214번 댓글"}
//];

var CommentBox = React.createClass({
	loadCommentsFromServer: function() {
		$.ajax({
			url: this.props.url,
			dataType: 'json',
			cache: false,
			success: function(data) {
				this.setState({data: data});
			}.bind(this),
			error: function(xhr, status, err) {
				alert("에러발생");
			}.bind(this)
		});
	},
	// 서버에 요청을 수행하고 목록 업데이트
	handleCommentSubmit: function(comment) {
		var comments = this.state.data;
	    $.ajax({
	        url: this.props.url,
	        dataType: 'json',
	        type: 'POST',
	        data: comment,
	        success: function(data) {
	            this.setState({data: data});
	        }.bind(this),
	        error: function(xhr, status, err) {
	            alert("에러발생2");
	        }.bind(this)
	    });
	},
	getInitialState: function() {
		return {data: []};
	},
	componentDidMount: function() {
		this.loadCommentsFromServer();
		setInterval(this.loadCommentsFromServer, this.props.pollInterval);
	},
	render: function() {
		return (
			<div className="commentBox">
				<h1 className="small">타이틀</h1>
				<CommentList data={this.state.data} />
				<CommentForm onCommnetSubmit={this.handleCommentSubmit} />
			</div>
		);
	}
});

var CommentList = React.createClass({
	render: function() {
		var commentNodes = this.props.data.map(function (comment) {
			return (
				<Comment author={comment.author}>
					{comment.text}
				</Comment>
			);
		});
		return (
			<div className="commentList">
				{commentNodes}
			</div>
		);
	}
});

var CommentForm = React.createClass({
	handleSubmit: function(e) {
		// 폼 submit에 대한 브라우저의 기본동작을 막기 위함
		e.priventDefault();
		// 컴포넌트를 참조하기 위해 this.refs.name 사용
		var author = React.findDOMNode(this.refs.author).value.trim();
		var text = React.findDOMNode(this.refs.text).value.trim();
		if(!text || !author) {
			return;
		}
		this.props.onCommentSubmit({author: author, text: text});
		React.findDOMNode(this.refs.author).value = '';
		React.findDOMNode(this.refs.text).value = '';
		return;
	},
	render: function() {
		return (
			// 이름지정을 위해 ref 속성 부여
			<form className="commentForm" onSubmit={this.handleSubmit}>
				<input type="text" placeholder="이름" ref="author" />
				<input type="text" placeholder="내용 입력" ref="text" />
				<input type="submit" value="올리기" />
			</form>
		)
	}
});

var Comment = React.createClass({
	render: function() {
		return (
			<div className="comment">
				<h2 className="commentAuthor">
					{this.props.author}
				</h2>
				{this.props.children}
			</div>
		)
	}
});

React.render(
	<CommentBox url="/static/json/example.json" pollInterval={1800000} />,
	document.getElementById('wrapper')
);