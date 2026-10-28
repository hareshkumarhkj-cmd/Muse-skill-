import {AbsoluteFill, Sequence} from 'remotion';
import {Hook} from './scenes/Hook';
import {Reveal} from './scenes/Reveal';
import {Climax} from './scenes/Climax';
import {EndCard} from './scenes/EndCard';
import {FontReady} from './components/Design';
import {timeline} from './timeline';

export const RaysShort01 = () => (
  <FontReady>
    <AbsoluteFill style={{backgroundColor: '#07121f'}}>
      <Sequence from={timeline.hook.from} durationInFrames={timeline.hook.duration}><Hook /></Sequence>
      <Sequence from={timeline.reveal.from} durationInFrames={timeline.reveal.duration}><Reveal /></Sequence>
      <Sequence from={timeline.climax.from} durationInFrames={timeline.climax.duration}><Climax /></Sequence>
      <Sequence from={timeline.end.from} durationInFrames={timeline.end.duration}><EndCard /></Sequence>
    </AbsoluteFill>
  </FontReady>
);
