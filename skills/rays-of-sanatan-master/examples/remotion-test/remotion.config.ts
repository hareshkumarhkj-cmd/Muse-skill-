import {Config} from '@remotion/cli/config';
import {existsSync} from 'node:fs';
import {delimiter, join} from 'node:path';

// Reuse a browser already on PATH; otherwise let Remotion download its browser.
// No machine-specific paths are stored in the project.
const browser = (process.env.PATH ?? '').split(delimiter)
  .flatMap((directory) => ['chromium', 'chromium-browser', 'google-chrome', 'chrome', 'chrome.exe'].map((name) => join(directory, name)))
  .find((candidate) => existsSync(candidate));
if (browser) Config.setBrowserExecutable(browser);

Config.setEntryPoint('./src/index.ts');
Config.setOutputLocation('out/rays-stone-test.mp4');
Config.setCodec('h264');
Config.setPixelFormat('yuv420p');
Config.setCrf(18);
Config.setConcurrency(2);
