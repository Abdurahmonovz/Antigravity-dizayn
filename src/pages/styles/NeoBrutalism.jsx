import React from 'react';
import Navigation from '../../components/Navigation';
import './NeoBrutalism.css';

export default function NeoBrutalism() {
  return (
    <div className="neo-brutalism-page">
      <Navigation 
        title="Neo-Brutalism" 
        description="Qalin qora chegaralar, yorqin ranglar, qattiq soyalar (hard shadow), assimetriya"
      />
      
      <main className="nb-main">
        <section className="nb-hero">
          <div className="nb-badge">YANGI TREND</div>
          <h1 className="nb-title">Xom va Erkin Dizayn</h1>
          <p className="nb-subtitle">Qoidalarni buzing. Oddiylikka qayting. Qattiq soyalar va qalin chiziqlar orqali o'ziga xoslikni yarating.</p>
          <button className="nb-button">Boshlash -&gt;</button>
        </section>

        <section className="nb-cards">
          <div className="nb-card bg-yellow">
            <h2 className="nb-card-title">Jasoratli Ranglar</h2>
            <p>Ko'zni qamashtiruvchi, yorqin va qat'iy ranglar palitrasi.</p>
          </div>
          <div className="nb-card bg-pink">
            <h2 className="nb-card-title">Qattiq Soyalar</h2>
            <p>Blur effektsiz, aniq burchakli qora soyalar.</p>
          </div>
          <div className="nb-card bg-blue">
            <h2 className="nb-card-title">Assimetriya</h2>
            <p>Mukammallikka intilmagan, erkin joylashuv.</p>
          </div>
        </section>
      </main>
      
      <footer className="nb-footer">
        <p>Neo-Brutalism Demo © 2026</p>
      </footer>
    </div>
  );
}
