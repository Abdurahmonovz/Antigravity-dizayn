import React from 'react';
import Navigation from '../../components/Navigation';
import './Neumorphism.css';

export default function Neumorphism() {
  return (
    <div className="neumorphism-page">
      <Navigation 
        title="Neumorphism" 
        description="Bir xil fon rangida bo'rtma va botiq soyalar"
      />
      
      <main className="neu-main">
        <section className="neu-hero neu-element">
          <h1>Yumshoq Interfeys (Soft UI)</h1>
          <p>Yorug'lik va soya orqali elementlarning fondan ajralib chiqishi. Hech qanday qattiq chiziqlar yo'q.</p>
          <div className="neu-buttons">
            <button className="neu-btn neu-flat">Bosib ko'ring</button>
            <button className="neu-btn neu-pressed">Bosilgan</button>
          </div>
        </section>

        <section className="neu-cards">
          <div className="neu-card neu-element">
            <div className="neu-icon neu-pressed">1</div>
            <h2>Bo'rtma Effekti</h2>
            <p>Element xuddi plastmassa kabi fondan bo'rtib chiqadi.</p>
          </div>
          <div className="neu-card neu-element">
            <div className="neu-icon neu-pressed">2</div>
            <h2>Botiq Effekti</h2>
            <p>Bosilganda element fon ichiga botib kiradi (inset shadow).</p>
          </div>
          <div className="neu-card neu-element">
            <div className="neu-icon neu-pressed">3</div>
            <h2>Bir xil Rang</h2>
            <p>Fon, tugma va kartochkalar barchasi bitta asosiy rangda bo'ladi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
