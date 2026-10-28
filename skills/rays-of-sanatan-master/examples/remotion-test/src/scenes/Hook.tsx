import {timeline} from '../timeline';
import {Caption, Shot} from '../components/Design';

export const Hook = () => (
  <Shot image="hook.png" frames={timeline.hook.duration} zoom={[1.02, 1.12]} origin="50% 38%">
    <Caption label="THE QUESTION" first="ये पत्थर" second="टिके कैसे हैं?" />
  </Shot>
);
