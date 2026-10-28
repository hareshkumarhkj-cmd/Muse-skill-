import {useEffect, useState, type ReactNode} from 'react';
import {AbsoluteFill, cancelRender, continueRender, delayRender, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';

export const gold = '#f4ce83';
export const hindi = '"Rays Devanagari", sans-serif';
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
export const progress = (f: number, a: number, b: number) => interpolate(f, [a, b], [0, 1], clamp);

// Bundle the environment's open-source Noto system sans font so Hindi remains
// readable on machines without Devanagari fonts. No network font request.
export const FontReady = ({children}: {children: ReactNode}) => {
  const [handle] = useState(() => delayRender('Loading bundled Hindi font'));
  useEffect(() => {
    let active = true;
    const font = new FontFace('Rays Devanagari', `url("${staticFile('fonts/NotoSansDevanagari-Bold.ttf')}")`, {weight: '700'});
    font.load().then((loaded) => {
      const fonts = document.fonts as FontFaceSet & {add(font: FontFace): FontFaceSet};
      fonts.add(loaded);
      if (active) continueRender(handle);
    }).catch((error: unknown) => cancelRender(error));
    return () => {active = false;};
  }, [handle]);
  return children;
};

export const Shot = ({image, frames, zoom, origin = '50% 50%', children, final = false}: {
  image: string; frames: number; zoom: [number, number]; origin?: string; children?: ReactNode; final?: boolean;
}) => {
  const f = useCurrentFrame();
  const p = progress(f, 0, frames - 1);
  const fadeOut = final ? 1 : 1 - progress(f, frames - 6, frames - 1) * 0.65;
  const fadeIn = final ? 1 : 0.5 + progress(f, 0, 7) * 0.5;
  return (
    <AbsoluteFill style={{overflow: 'hidden', color: '#fff6e3', fontFamily: 'Arial, sans-serif'}}>
      <AbsoluteFill style={{opacity: fadeIn * fadeOut}}>
        <Img src={staticFile(image)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${zoom[0] + (zoom[1] - zoom[0]) * p})`, transformOrigin: origin}} />
        <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(3,12,24,.65) 0%, transparent 23%, transparent 52%, rgba(3,12,24,.2) 64%, rgba(3,12,24,.94) 89%, #050e19 100%)'}} />
        <AbsoluteFill style={{boxShadow: 'inset 0 0 150px 25px rgba(0,0,0,.35)'}} />
        {Array.from({length: 17}, (_, i) => (
          <div key={i} style={{position: 'absolute', width: 2 + (i % 3), height: 2 + (i % 3), borderRadius: '50%', background: gold, opacity: 0.12 + (i % 4) * 0.08, left: `${(i * 47 + 13) % 100}%`, top: `${((i * 19 + 5) % 100 + 100 - f * (0.012 + i * 0.001)) % 100}%`, boxShadow: '0 0 10px #f4ce83'}} />
        ))}
      </AbsoluteFill>
      <div style={{position: 'absolute', top: 118, left: 72, display: 'flex', alignItems: 'center', gap: 19}}>
        <svg width="51" height="51" viewBox="0 0 64 64" aria-hidden><circle cx="32" cy="32" r="20" fill="none" stroke={gold} strokeWidth="2" />{Array.from({length: 12}, (_, i) => <path key={i} d="M32 2V9" stroke={gold} strokeWidth="2" transform={`rotate(${i * 30} 32 32)`} />)}<path d="M22 38 32 19 42 38Z" stroke={gold} fill="none" strokeWidth="2" /></svg>
        <div style={{fontSize: 24, letterSpacing: 4, color: gold, fontWeight: 700}}>RAYS OF SANATAN</div>
      </div>
      {children}
      <div style={{position: 'absolute', left: 72, bottom: 145, color: '#c7c9cc', fontFamily: hindi, fontWeight: 700, fontSize: 22}}>काल्पनिक दृश्य • AI-निर्मित चित्र</div>
    </AbsoluteFill>
  );
};

export const Caption = ({label, first, second, delay = 3}: {label: string; first: string; second: string; delay?: number}) => {
  const f = useCurrentFrame();
  const enter = progress(f, delay, delay + 12);
  return (
    <div style={{position: 'absolute', left: 72, right: 100, bottom: 262, opacity: enter, transform: `translateY(${(1 - enter) * 24}px)`}}>
      <div style={{display: 'flex', alignItems: 'center', gap: 18, marginBottom: 26}}><div style={{height: 3, width: 48, background: gold}} /><div style={{fontSize: 23, letterSpacing: 5, color: gold, fontWeight: 700}}>{label}</div></div>
      <div style={{fontFamily: hindi, fontSize: 77, lineHeight: 1.46, fontWeight: 700, textShadow: '0 3px 18px #000'}}>{first}<br /><span style={{color: gold}}>{second}</span></div>
    </div>
  );
};
