import React from 'react';
import Navigation from '../../components/Navigation';
import './DarkModeLuxury.css';

export default function DarkModeLuxury() {
  return (
    <div className="dark-luxury-page">
      <Navigation 
        title="Dark Mode Luxury" 
        description="Qora fon, oltin/kumush aksent ranglar, nafis tipografika"
      />
      
      <main className="luxury-main">
        <section className="luxury-hero">
          <div className="glow-effect"></div>
          <h1>Nafosat va Lyuks</h1>
          <p>Chuqur qorong'ulik ichida porlovchi oltin zarralar. Premium brendlar tanlovi.</p>
          <button className="luxury-btn">Koleksiyani Ko'rish</button>
        </section>

        <section className="luxury-cards">
          <div className="luxury-card">
            <div className="luxury-line"></div>
            <h2>Qora Fon</h2>
            <p>Sof qora (#000000) yoki juda to'q kulrang fon oqlangan muhit yaratadi.</p>
          </div>
          <div className="luxury-card">
            <div className="luxury-line"></div>
            <h2>Oltin Urg'u</h2>
            <p>Yengil gradientli oltin rang detayllarga diqqatni tortadi.</p>
          </div>
          <div className="luxury-card">
            <div className="luxury-line"></div>
            <h2>Serif Shriftlar</h2>
            <p>Klassik va nafis serif shriftlar qimmatbaho tuyg'u beradi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
