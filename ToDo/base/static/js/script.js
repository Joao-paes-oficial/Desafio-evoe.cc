$(document).ready(() => {
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', () => {
        searchForm.submit();
    });
})