import React from 'react';
import Navigation from '../../components/Navigation';
import './CyberpunkSynthwave.css';

export default function CyberpunkSynthwave() {
  return (
    <div className="cp-page">
      <Navigation title="Cyberpunk / Synthwave" description="Neon nur effektlari, qorong'i fon, elektr ranglar" />
      <main className="cp-main">
        <section className="cp-hero">
          <h1 className="cp-glitch">NIGHT CITY</h1>
          <p>High tech, low life. Neon chiroqlar bilan yoritilgan kelajak shahri.</p>
          <button className="cp-btn">SYSTEM_HACK</button>
        </section>

        <section className="cp-cards">
          <div className="cp-card">
            <h2>Neon Nurlar</h2>
            <p>Qorong'i fonda yonib turuvchi sariq, moviy va pushti neon chiziqlar.</p>
          </div>
          <div className="cp-card">
            <h2>Texnologik UI</h2>
            <p>HUD va gologrammalarni eslatuvchi kesilgan burchaklar.</p>
          </div>
        </section>
      </main>
    </div>
  );
}