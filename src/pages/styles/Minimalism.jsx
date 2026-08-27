import React from 'react';
import Navigation from '../../components/Navigation';
import './Minimalism.css';

export default function Minimalism() {
  return (
    <div className="minimalism-page">
      <Navigation 
        title="Minimalism" 
        description="Ko'p bo'sh joy, oq fon, aniq tipografika, minimal ranglar"
      />
      
      <main className="min-main">
        <section className="min-hero">
          <h1>Kamroq. Yaxshiroq.</h1>
          <p>Faqat eng kerakli narsalar. Ortiqcha bezaklarsiz, sof funksionallik.</p>
        </section>

        <section className="min-grid">
          <div className="min-item">
            <span className="min-number">01</span>
            <h2>Bo'sh Joy</h2>
            <p>Oq bo'shliq (white space) dizaynning faol elementiga aylanadi.</p>
          </div>
          <div className="min-item">
            <span className="min-number">02</span>
            <h2>Tipografika</h2>
            <p>Katta va o'qishli shriftlar ma'lumot ierarxiyasini belgilaydi.</p>
          </div>
          <div className="min-item">
            <span className="min-number">03</span>
            <h2>Monoxrom</h2>
            <p>Asosan oq va qora. Rang faqat urg'u berish uchun ishlatiladi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
