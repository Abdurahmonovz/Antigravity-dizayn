import React from 'react';
import Navigation from '../../components/Navigation';
import './KineticTypography.css';

export default function KineticTypography() {
  return (
    <div className="kt-page">
      <Navigation title="Kinetic Typography" description="Harakatlanuvchi matn" />
      <main className="kt-main">
        <div className="marquee">
          <div className="marquee-inner">
            <span>MOTION IS EMOTION • TYPOGRAPHY • </span>
            <span>MOTION IS EMOTION • TYPOGRAPHY • </span>
          </div>
        </div>
        <div className="marquee reverse">
          <div className="marquee-inner">
            <span>DESIGN THAT MOVES • ANIMATION • </span>
            <span>DESIGN THAT MOVES • ANIMATION • </span>
          </div>
        </div>
      </main>
    </div>
  );
}