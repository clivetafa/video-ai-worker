# video-ai-worker (test stub)

This is a placeholder RunPod Serverless worker. It does **not** generate
real AI video yet — it waits 10 seconds and returns a small public-domain
sample video, so you can confirm the full chain works:

```
your website  →  RunPod /run  →  RunPod /status  →  video_url  →  plays in browser
```

Once this is confirmed working end to end, `handler.py` gets replaced
with real video generation (the model code from your Colab notebook,
containerized).

## Deploying this to RunPod

1. Push this folder to a **new GitHub repo** (see step-by-step guide from
   Claude in the chat — don't do this part from memory, follow along).
2. In the RunPod console, go to **Serverless → New Endpoint**.
3. Choose **GitHub Repo** as the source and connect/select this repo.
4. RunPod builds the Docker image for you automatically — no local Docker
   needed.
5. Pick a GPU tier (even the cheapest option works fine for this test
   stub, since it isn't doing real GPU work yet).
6. Once deployed, copy the **Endpoint ID** from the endpoint's details
   page into your website's `.env.local` as `RUNPOD_ENDPOINT_ID`.

## Testing it

From your website's "Generate video" page: type anything, hit Generate,
wait about 10-15 seconds, and you should see the sample Big Buck Bunny
clip play. That confirms the connection works.
