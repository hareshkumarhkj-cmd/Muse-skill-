import {timeline} from '../timeline';
import {Caption, Shot} from '../components/Design';

export const Climax = () => (
  <Shot image="hero.png" frames={timeline.climax.duration} zoom={[1.13, 1.015]} origin="50% 35%">
    <Caption label="THE BIG PICTURE" first="छोटे जोड़।" second="विराट रचना।" />
  </Shot>
);
