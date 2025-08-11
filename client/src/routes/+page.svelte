<script lang="ts">
  import { PUBLIC_API_URL } from '$env/static/public';

  let files: FileList | undefined = $state(undefined);
  let value: string = $state('');
  let can_send = $derived.by(() => {
    if (files) {
      return files.length > 0;
    }
    return false;
  });

  let post_track_promise: Promise<void> | undefined = $state(undefined);
  let meshes: { name: string; blob: Blob; url: string }[] = $state([]);
  const postTrack = async () => {
    if (files === undefined) {
      return;
    }
    if (files.length === 0) {
      return;
    }
    const body = await files.item(0)!.bytes();

    let res = await fetch(`${PUBLIC_API_URL}/track`, { body, method: 'POST' });
    const blob = await res.blob();
    meshes.push({ name: files.item(0)!.name, blob, url: URL.createObjectURL(blob) });
    files = undefined;
    value = '';
  };
</script>

<div class="mt-3 flex flex-col items-center gap-3">
  <label for="track">Upload a .gpx file:</label>
  <input
    accept=".gpx"
    bind:files
    bind:value
    id="track"
    name="track"
    type="file"
    class="file-input"
  />
  <button
    class="btn btn-primary"
    disabled={!can_send}
    onclick={() => {
      post_track_promise = postTrack();
    }}
  >
    {#if post_track_promise}
      {#await post_track_promise}
        <span class="loading loading-spinner"></span>
        generating
      {:then}
        Send
      {/await}
    {:else}
      Send
    {/if}
  </button>

  <h2>Meshes</h2>
  {#each meshes as mesh}
    <a href={mesh.url} download={mesh.name.replace('.gpx', '.stl')}
      >{mesh.name.replace('.gpx', '.stl')}
    </a>
  {:else}
    <i>No mesh yet</i>
  {/each}
</div>
