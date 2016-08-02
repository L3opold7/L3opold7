
function delete_user(username, token) {
    var result = confirm('정말 계정을 삭제하시겠습니까?\n복구는 없습니다');
    if(result) {
        $.ajax({
            method: "POST",
            url: "/user/" + username + "/delete/",
            data: { csrfmiddlewaretoken: token }
        }).done(function(res) {
            alert('계정을 삭제했습니다\n좋은 인연이였습니다');
            location.replace('/');
        }).fail(function(res) {
            alert('잘못된 요청입니다');
        });
    } else {

    }
}