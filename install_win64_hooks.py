#!/usr/bin/env python3
import gclient

DISABLED_SHELL = [
  'build/util/lastchange.py',
  'v8/test/fuzzer/wasm_corpus.tar.gz.sha1',
  'content/test/gpu/gpu_tests/mediapipe_update.py',
  'testing/generate_location_tags.py'
]

if __name__ == '__main__':
  SKIP_PATH_PREFIX='src/'
  options, _ = gclient.OptionParser().parse_args([])
  obj = gclient.GClient.LoadCurrentConfig(options)
  obj.GetCipdRoot()
  sol = obj.dependencies[0]
  sol.ParseDepsFile()
  hooks = sol.GetHooks(options)
  for hook in hooks:
    hook._action = tuple([cmd.replace(SKIP_PATH_PREFIX, '', 1) if SKIP_PATH_PREFIX in cmd else cmd for cmd in hook._action])
    runer = " ".join(hook._action)
    print(runer)
    should_skips = [shell in runer for shell in DISABLED_SHELL] 
    if any(should_skips):
      print('skiped')
      continue
    hook.run()