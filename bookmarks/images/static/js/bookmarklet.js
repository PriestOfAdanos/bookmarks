(function()
var jquery_version = '2.1.4';
var site_url = 'htttp://127.0.0.1:8000';
var static_url = site_url + 'static/';
var min_width = 100;
var = min_height;

function bookmarklet(msg){
if(typeof window.jQuery != 'undefined'){
bookmarklet();
}else{
var conflict = typeof window.$ !='undefined';
var script = document.createElement('script');
script.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery'+jquery_version + '/jquery.min.js');
document.getElementBytagName('head')[0].appendChild(script);
var attempts = 15;
(function(){
if(typeof window.jQuery == 'undefined'){
if(--attempts>0){
window.setTimeout(arguments.calee, 250)
}else{
alert('Wystąpił błąd')
}
}else{
bookmarklet();
}
})();
}
}
function bookmarklet(msg){
var css = jQuery('<link>');
css.attr({
rel: 'stylesheet',
type: 'text/css'
href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)

});
jQuery('head').append(css);
box_html='<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Wybierz obraz</h1><div class="images"></div></div>';
jQuery('body').append(box_html);
jQuery('#bookmarklet #close').click(function(){
jQuery('#bookmarklet').remove();
});
jQuery.each(jQuery('img[src$="jpg"]'), function(index,image){
if(jQuery(image).widh()>=min_width && jQuery(image).height()>= min_height){
image_url = jQuery(image).attr('src');
jQuery('#bookmarklet .images').append('<a href="#"><img src="'+image_url+'"/></a>');
}
});
jQuery('#bookmarklet .images a').click(function(e){
selected_image = jQuery(this).children('img').attr('src');
jQuery('#bookmarklet').hide;
window.open(site_url+'images/create/?url='+encodeURIComponent(selected_image)
+'&title'
+encodeURIComponent(jQuery('title').text()),
'_blank')
})
};
jQuery('#')
)()
