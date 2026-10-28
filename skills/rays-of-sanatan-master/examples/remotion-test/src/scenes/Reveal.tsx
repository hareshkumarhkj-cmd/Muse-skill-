import {timeline} from '../timeline';
import {useCurrentFrame} from 'remotion';
import {Caption, progress, Shot} from '../components/Design';

export const Reveal = () => {
  const f = useCurrentFrame();
  const opacity = progress(f, 14, 28) * (1 - progress(f, 128, 144));
  return (
    <Shot image="detail.png" frames={timeline.reveal.duration} zoom={[1.12, 1.025]} origin="50% 42%">
      <svg viewBox="0 0 1080 1920" style={{position: 'absolute', inset: 0, width: '100%', height: '100%', opacity, filter: 'drop-shadow(0 0 8px #40dfff)'}} aria-hidden>
        <g stroke="#74eaff" strokeWidth="3" fill="none" opacity=".65">
          <path d="M145 620V555H215 M865 555H935V620 M145 1060V1125H215 M865 1125H935V1060" />
          <path d="M165 1200H915" strokeDasharray="9 14" opacity=".35" />
          <path d={`M165 ${630 + progress(f, 22, 120) * 430}H915`} opacity=".22" />
        </g>
      </svg>
      <Caption label="LOOK CLOSER" first="हर जोड़ में" second="छिपा है संतुलन।" />
    </Shot>
  );
};
