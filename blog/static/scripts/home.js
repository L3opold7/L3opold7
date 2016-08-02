
function yeah() {
    var data = $(".search-with-tag").val();
    location.replace('/post/tag/' + data);
    return false;
}