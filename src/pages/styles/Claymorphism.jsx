import React from 'react';
import Navigation from '../../components/Navigation';
import './Claymorphism.css';

export default function Claymorphism() {
  return (
    <div className="claymorphism-page">
      <Navigation 
        title="Claymorphism" 
        description="3D, 'loydan yasalgan' kabi yumshoq va bo'rtib turgan elementlar"
      />
      
      <main className="clay-main">
        <section className="clay-hero clay-card">
          <h1>Loy Effekti</h1>
          <p>Yumshoq ichki va tashqi soyalar tufayli yuzaga keladigan quvnoq, 3D hajm.</p>
          <button className="clay-btn">Ushlab ko'ring</button>
        </section>

        <section className="clay-cards">
          <div className="clay-card clay-yellow">
            <div className="clay-icon">🎈</div>
            <h2>Yumshoq Burchaklar</h2>
            <p>O'ta yumaloq burchaklar va qalin border-radius.</p>
          </div>
          <div className="clay-card clay-pink">
            <div className="clay-icon">🧸</div>
            <h2>Ichki Soyalar</h2>
            <p>Pastki o'ng va yuqori chap burchaklardagi ikkita inset shadow orqali hajm.</p>
          </div>
          <div className="clay-card clay-blue">
            <div className="clay-icon">☁️</div>
            <h2>Suzuvchi Ob'ektlar</h2>
            <p>Pastdagi katta va xira soya orqali havoda osilib turgandek effekt.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
