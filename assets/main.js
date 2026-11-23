'use strict';
(function(){
 const button=document.querySelector('.menu-button');
 const nav=document.querySelector('.nav');
 if(!button||!nav)return;
 const close=()=>{button.setAttribute('aria-expanded','false');nav.classList.remove('open');};
 button.addEventListener('click',()=>{
  const open=button.getAttribute('aria-expanded')==='true';
  button.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open);
 });
 nav.addEventListener('click',e=>{if(e.target.closest('a'))close();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')close();});
 document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!button.contains(e.target))close();});
})();
