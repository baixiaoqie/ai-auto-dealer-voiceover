<template>
  <div class="app-container">
    <header class="app-header">
      <div class="header-content">
        <div class="logo-section">
          <div class="logo-accent"></div>
          <h1 class="brand-title">
            <span class="brand-subtitle">AI</span>
            <span class="brand-main">智能口播</span>
          </h1>
        </div>
        <div class="header-decoration">
          <div class="decoration-line"></div>
          <span class="decoration-text">AUTOMOTIVE EXCELLENCE</span>
        </div>
      </div>
    </header>
    
    <main class="app-main">
      <router-view />
    </main>
    
    <footer class="app-footer">
      <div class="footer-content">
        <div class="footer-line"></div>
        <p class="footer-text">PRECISION ENGINEERED FOR DEALERSHIP SUCCESS</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  position: relative;
}

.app-header {
  background: linear-gradient(180deg, rgba(18, 18, 26, 0.95) 0%, rgba(18, 18, 26, 0.85) 100%);
  border-bottom: 1px solid var(--border-subtle);
  padding: 0;
  position: relative;
  backdrop-filter: blur(10px);
}

.header-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 32px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 20px;
}

.logo-accent {
  width: 4px;
  height: 60px;
  background: linear-gradient(180deg, var(--accent-gold) 0%, var(--accent-gold-dark) 100%);
  border-radius: 2px;
}

.brand-title {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin: 0;
}

.brand-subtitle {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 4px;
  color: var(--accent-gold);
  text-transform: uppercase;
}

.brand-main {
  font-family: 'Playfair Display', 'Noto Serif SC', serif;
  font-size: 32px;
  font-weight: 700;
  letter-spacing: 2px;
  color: var(--text-primary);
}

.header-decoration {
  display: flex;
  align-items: center;
  gap: 20px;
}

.decoration-line {
  width: 80px;
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, var(--accent-gold) 50%, transparent 100%);
}

.decoration-text {
  font-family: 'Montserrat', sans-serif;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 3px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.app-main {
  flex: 1;
  padding: 60px 40px;
}

.app-footer {
  padding: 40px;
  border-top: 1px solid var(--border-subtle);
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.footer-line {
  width: 60px;
  height: 2px;
  background: var(--accent-gold);
}

.footer-text {
  font-family: 'Montserrat', sans-serif;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 4px;
  color: var(--text-muted);
  text-transform: uppercase;
  margin: 0;
}

@media (max-width: 768px) {
  .header-content {
    padding: 24px 20px;
    flex-direction: column;
    gap: 20px;
    text-align: center;
  }
  
  .app-main {
    padding: 40px 20px;
  }
  
  .decoration-text {
    display: none;
  }
}
</style>
