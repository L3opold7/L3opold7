var had = 0;

function vote(id, what, token) {
    if(had === 1) {
        alert('Already voted!');
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
            alert('Complete voted!');
        }).fail(function(res) {
            alert('Wrong Request');
        });
    }
}

function del(id, token) {
    var result = confirm('Are you sure?');
    if(result) {
        $.ajax({
            method: "POST",
            url: "/post/" + id + "/delete/",
            data: { csrfmiddlewaretoken: token }
        }).done(function(res) {
            alert('Complete deleted Post!');
            location.replace('/post/');
        }).fail(function(res) {
            alert("Wrong Request");
        });
    } else {

    }
}