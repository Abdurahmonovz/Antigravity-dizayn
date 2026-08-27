import React from 'react';
import Navigation from '../../components/Navigation';
import './Skeuomorphism.css';

export default function Skeuomorphism() {
  return (
    <div className="skeuo-page">
      <Navigation title="Skeuomorphism" description="Real dunyodagi ob'ektlarga o'xshash teksturalar" />
      <main className="skeuo-main">
        <div className="skeuo-switch">
          <div className="skeuo-switch-inner">ON</div>
        </div>
        <div className="skeuo-panel">
          <h1>Analog Interfeys</h1>
          <p>Yog'och teksturalar, charm va metall detallar.</p>
          <button className="skeuo-btn">BOSISH</button>
        </div>
      </main>
    </div>
  );
}