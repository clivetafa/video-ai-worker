"""
TEST WORKER — proves the RunPod <-> website connection works end to end.

This does NOT generate real AI video yet. It waits a bit (to simulate
render time) and returns a small public-domain sample video. Once this
is confirmed working from your website, we replace the body of this
function with real video generation.

Matches the contract lib/runpod.ts expects:
  input:  { topic, video_length_seconds, clip_length_seconds, num_clips }
  output: { video_url }
"""

import time
import runpod


def handler(job):
    job_input = job.get("input", {})
    topic = job_input.get("topic", "")
    video_length_seconds = job_input.get("video_length_seconds", 300)

    print(f"[test-worker] Received job. topic={topic!r} "
          f"video_length_seconds={video_length_seconds}")

    # Simulate render time so you can see the "rendering" state in the UI.
    # Real video generation will take much longer than this.
    time.sleep(10)

    return {
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "note": "Placeholder test video. Swap handler.py for real generation next.",
        "topic_received": topic,
    }


runpod.serverless.start({"handler": handler})
