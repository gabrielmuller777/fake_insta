$('[data-role = like_form]').on('click', '[data-action = like_btn]' function(e){
    e.preventDefault();
    var $like_form = $(e.delegateTarget);
    var $like_btn = $(e.currentTarget);
    var url = $like_form.data('url');
    var pk =  $like_btn.data('id');
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'pk': pk,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response){
            $('#like_post').html(response['form'])
        },
        error: function(rs, e){
            console.log(rs.responseText);
        },
    });
});