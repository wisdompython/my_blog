const loadBtn=  document.getElementById('add-btn')
const total_post = JSON.parse(document.getElementById('json-total').textContent);              
const alert = document.getElementById('alert')

function loadmorePost(){
    const content_container = document.getElementById('blog-content');
    var _current_item =$('.post').length;
    $.ajax({
            url:$('.add-more').attr('data-url'),
            type:'GET',
            data:{
                    'total_item':_current_item
            },
            
            beforeSend:function(){
                alert.classList.add('no-more-data')

            },
            success:function(response){
                    const data = response.posts
                    alert.classList.add('no-more-data')

                    
                    data.forEach(posts => {
                            const imageurl = 'media/'+posts.image;
                            const detailurl = 'post/'+posts.id;

                            content_container.innerHTML +=`<div class="post" id=${posts.id}>
                                                                    <img id="img-src" src=${imageurl} image-url="{{post.image.url}alt="">
                                                                    <p><strong>${posts.title}</strong></p>
                                                                        <h3>${posts.category__name}</h3>
                                                                    
                                                                    <a  id="post-detail-link" href=${detailurl}><h2>${posts.summary}</h2></a>
                                                            </div>`
                    })

                    if (_current_item == total_post){
                       
                    alert.classList.remove('no-more-data')
                    loadBtn.classList.add('no-more-data')
                    }
                    else{ loadBtn.classList.remove('no-more-data')
                    alert.classList.add('no-more-data')
                    }

            },
            error:function(err){
                    console.log(err);

            },

    });

};
loadBtn.addEventListener('click', () => {
    loadmorePost()
});
