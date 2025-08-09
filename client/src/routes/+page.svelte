<script lang="ts">
  import { PUBLIC_API_URL } from '$env/static/public';

  let files: FileList | undefined = $state();
  let can_send = $derived.by(() => {
    if (files) {
      return files.length > 0;
    }
    return false;
  });

  const postTrack = async () => {
    if (files === undefined) {
      return;
    }
    if (files.length === 0) {
      return;
    }
    const body = await files.item(0)!.bytes();

    let res = await fetch(`${PUBLIC_API_URL}/track`, { body, method: 'POST' });
    console.log(res);
  };
</script>

<div class="mt-3 flex flex-col items-center gap-3">
  <label for="track">Upload a .gpx file:</label>
  <input accept=".gpx" bind:files id="track" name="track" type="file" class="file-input" />
  <button class="btn btn-primary" disabled={!can_send} onclick={postTrack}>Send</button>
</div>
