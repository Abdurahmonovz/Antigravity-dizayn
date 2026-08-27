import React from 'react';
import Navigation from '../../components/Navigation';
import './Glassmorphism.css';

export default function Glassmorphism() {
  return (
    <div className="glass-page">
      <div className="glass-blob blob-1"></div>
      <div className="glass-blob blob-2"></div>
      <div className="glass-blob blob-3"></div>
      
      <Navigation 
        title="Glassmorphism" 
        description="Shaffof, xira (blur) fon, oyna effekti, yumshoq gradientlar"
      />
      
      <main className="glass-main">
        <section className="glass-hero glass-panel">
          <h1 className="glass-title">Oyna Effekti</h1>
          <p className="glass-subtitle">Shaffoflik va fon xiralashuvi (background-blur) orqali chuqurlik hissini yaratish.</p>
          <button className="glass-button">Batafsil ma'lumot</button>
        </section>

        <section className="glass-cards">
          <div className="glass-card glass-panel">
            <div className="glass-icon">✧</div>
            <h2>Shaffoflik</h2>
            <p>Elementlar orqasidagi fon biroz ko'rinib turadi.</p>
          </div>
          <div className="glass-card glass-panel">
            <div className="glass-icon">❂</div>
            <h2>Blur Effekti</h2>
            <p>Orqa fon xiralashib, oldingi qatlamga e'tiborni tortadi.</p>
          </div>
          <div className="glass-card glass-panel">
            <div className="glass-icon">✦</div>
            <h2>Oq Chegaralar</h2>
            <p>Yupqa va yarim shaffof oq chegaralar shisha qirrasini eslatadi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
