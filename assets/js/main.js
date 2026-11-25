(function(){
var els=[].slice.call(document.querySelectorAll('[data-r]'));
var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function show(el,d){el.style.setProperty('--d',d+'s');el.classList.add('in');setTimeout(function(){el.classList.add('done')},d*1000+1100)}
if(rm||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in','done')})}
else{
 var io=new IntersectionObserver(function(es){var n=0;es.forEach(function(en){
  if(!en.isIntersecting)return;var el=en.target;io.unobserve(el);
  show(el,el.dataset.d!==undefined?+el.dataset.d:Math.min(n++*.08,.5));
 })},{rootMargin:'0px 0px -8% 0px',threshold:.05});
 els.forEach(function(e){io.observe(e)});
}
[].forEach.call(document.querySelectorAll('[data-back]'),function(a){a.addEventListener('click',function(e){
 try{if(history.length>1&&document.referrer&&new URL(document.referrer).origin===location.origin){e.preventDefault();history.back()}}catch(x){}
})});
})();
