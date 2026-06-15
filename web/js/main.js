/**
 * 个人介绍网站 - 交互脚本
 * DevOps Lab Project
 */

document.addEventListener('DOMContentLoaded', () => {

  // --- 平滑滚动（兼容不支持 CSS scroll-behavior 的浏览器） ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // --- 导航栏滚动时添加阴影 ---
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
        navbar.style.boxShadow = '0 2px 8px rgba(0,0,0,0.08)';
      } else {
        navbar.style.boxShadow = 'none';
      }
    });
  }

  // --- 技能卡片渐入动画 (Intersection Observer) ---
  const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -50px 0px',
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.skill-card, .interest-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });

  // --- 更新页脚年份 ---
  const footerYear = document.querySelector('.footer p');
  if (footerYear) {
    const year = new Date().getFullYear();
    footerYear.textContent = footerYear.textContent.replace('2026', year);
  }

  console.log('🎉 Personal portfolio website loaded! DevOps Lab Project');
});
