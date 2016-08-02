
function delete_user(username, token) {
    var result = confirm('Are you sure?');
    if(result) {
        $.ajax({
            method: "POST",
            url: "/user/" + username + "/delete/",
            data: { csrfmiddlewaretoken: token }
        }).done(function(res) {
            alert('Complete deleted User!!');
            location.replace('/');
        }).fail(function(res) {
            alert('Wrong Request');
        });
    } else {

    }
}