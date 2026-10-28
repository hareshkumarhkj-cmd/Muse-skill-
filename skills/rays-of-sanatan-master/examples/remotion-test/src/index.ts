import {createElement} from 'react';
import {Composition, registerRoot} from 'remotion';
import {RaysShort01} from './RaysShort01';
import {videoSpec} from './timeline';

export const RemotionRoot = () => createElement(Composition, {
  id: videoSpec.composition_id,
  component: RaysShort01,
  durationInFrames: videoSpec.duration_frames,
  fps: videoSpec.fps,
  width: videoSpec.width,
  height: videoSpec.height,
});

registerRoot(RemotionRoot);
