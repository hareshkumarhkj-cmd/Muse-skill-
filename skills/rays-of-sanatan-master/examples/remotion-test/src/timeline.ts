import contract from '../production-contract.json';

export const videoSpec = contract.project;
export const timeline: Record<string, {from: number; duration: number}> = Object.fromEntries(
  contract.scenes.map((scene) => [scene.id, {
    from: scene.start_frame,
    duration: scene.end_frame - scene.start_frame,
  }]),
);
