let subreddits = [
    'dogpictures',
    'eyebleach',
    'corgi',
    'puppies'
];

$.ajax({
  url:"https://www.reddit.com/r/" + "corgi" +"/top/.json",
  success:function(response){
    console.log("response");
  },
  error:function(response){
    console.log("response");
  }
});

function get_subreddit_image_urls(subreddit){

}

$('#photos').html("Hi");
console.log(get_subreddit_image_urls('corgi'));
