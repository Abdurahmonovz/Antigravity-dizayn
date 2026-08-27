import React from 'react';
import Navigation from '../../components/Navigation';
import './MaterialDesign.css';

export default function MaterialDesign() {
  return (
    <div className="material-page">
      <Navigation 
        title="Material Design" 
        description="Google uslubi: soyalar, elevatsiya, dumaloq burchaklar, ripple effektlar"
      />
      
      <main className="md-main">
        <header className="md-appbar md-elevation-4">
          <div className="md-toolbar">
            <h2>Material Ilovalar</h2>
            <button className="md-icon-btn">⋮</button>
          </div>
        </header>

        <section className="md-content">
          <div className="md-hero md-elevation-1">
            <h1>Elevatsiya va Soya (Depth)</h1>
            <p>Qatlamlarning balandligini (z-index) bildirish uchun turli darajadagi yumshoq soyalardan foydalaniladi.</p>
            
            <button className="md-fab md-elevation-6">+</button>
          </div>

          <div className="md-grid">
            <div className="md-card md-elevation-1">
              <div className="md-card-media"></div>
              <div className="md-card-title">Asosiy Qatlam</div>
              <div className="md-card-text">Barcha elementlar mantiqiy kartochkalarda joylashadi. Hover qilinganda soya ko'payadi.</div>
              <div className="md-card-actions">
                <button className="md-btn-text">Tanishish</button>
                <button className="md-btn-text">Ulashish</button>
              </div>
            </div>
            
            <div className="md-card md-elevation-1">
              <div className="md-card-media bg-accent"></div>
              <div className="md-card-title">Interaktivlik</div>
              <div className="md-card-text">Tugmalar bosilganda ripple (to'lqin) effekti va rang o'zgarishi interaktivlikni oshiradi.</div>
              <div className="md-card-actions">
                <button className="md-btn-text">Tanishish</button>
                <button className="md-btn-text">Ulashish</button>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
