(function(){
  const toggle = document.getElementById('theme-toggle');
  const iconSun = document.getElementById('icon-sun');
  const iconMoon = document.getElementById('icon-moon');

  // read saved or system preference
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  if(saved === 'dark' || (!saved && prefersDark)){
    document.documentElement.classList.add('dark');
    iconSun.classList.add('d-none');
    iconMoon.classList.remove('d-none');
  } else {
    document.documentElement.classList.remove('dark');
    iconSun.classList.remove('d-none');
    iconMoon.classList.add('d-none');
  }

  toggle.addEventListener('click', function(){
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    if(isDark){
      iconSun.classList.add('d-none');
      iconMoon.classList.remove('d-none');
    } else {
      iconSun.classList.remove('d-none');
      iconMoon.classList.add('d-none');
    }
  });
})();
