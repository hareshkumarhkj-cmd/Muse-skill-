import {timeline} from '../timeline';
import {AbsoluteFill} from 'remotion';
import {Caption, Shot} from '../components/Design';

export const EndCard = () => (
  <Shot image="hero.png" frames={timeline.end.duration} zoom={[1.015, 1.015]} final>
    <AbsoluteFill style={{background: 'rgba(3,12,24,.42)'}} />
    <Caption label="RAYS OF SANATAN" first="कला या इंजीनियरिंग?" second="दोनों।" delay={0} />
  </Shot>
);
