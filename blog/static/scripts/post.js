var had = 0;

function vote(id, what, token) {
    if(had === 1) {
        alert('이미 투표하셨습니다');
    } else {
        $.ajax({
            method: "POST",
            url: "/post/" + id + "/vote/",
            data: { what: what, csrfmiddlewaretoken: token }
        }).done(function(res) {
            had = 1;

            if(what == 'up') {
                var numb = Number($(".vote-number").text()) + 1
            } else if(what == 'down') {
                var numb = Number($(".vote-number").text()) - 1
            }
            $(".vote-number").text(numb)
            alert('투표하셨습니다');
        }).fail(function(res) {
            alert('잘못된 요청입니다');
        });
    }
}

function del(id, token) {
    var result = confirm('정말 삭제하시겠어요?');
    if(result) {
        $.ajax({
            method: "POST",
            url: "/post/" + id + "/delete/",
            data: { csrfmiddlewaretoken: token }
        }).done(function(res) {
            alert('삭제했습니다');
            location.replace('/post/');
        }).fail(function(res) {
            alert('잘못된 요청입니다');
        });
    } else {

    }
}