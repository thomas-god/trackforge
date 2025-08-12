<script module>
  export interface Mesh {
    name: string;
    data: Blob;
    url: string;
  }
</script>

<script lang="ts">
  import { PUBLIC_API_URL } from '$env/static/public';
  import Download from '../components/atoms/icons/Download.svelte';
  import View from '../components/atoms/icons/View.svelte';
  import MeshViewer from '../components/molecules/MeshViewer.svelte';

  let files: FileList | undefined = $state(undefined);
  let value: string = $state('');
  let can_send = $derived.by(() => {
    if (files) {
      return files.length > 0;
    }
    return false;
  });

  let post_track_promise: Promise<void> | undefined = $state(undefined);
  let mesh: Mesh | undefined = $state(undefined);
  let showMesh = $state(false);

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
    const url = URL.createObjectURL(blob);
    const name = files.item(0)!.name.replace('.gpx', '.stl');
    mesh = { name, data: blob, url };

    files = undefined;
    value = '';
  };

  let styles = getComputedStyle(document.documentElement);
  let color = styles.getPropertyValue('--color-base-content');
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

  {#if mesh !== undefined}
    <div class="flex flex-row items-center gap-2 p-2">
      {mesh.name} ({Math.round(mesh.data.size / 1024 / 1024)} MB)
      <button onclick={() => (showMesh = !showMesh)} class="btn btn-square btn-ghost">
        <View {color} title="Visualize mesh" /></button
      >
      <a href={mesh.url} download={mesh.name} class="btn btn-square btn-ghost">
        <Download {color} title="Download .stl file" />
      </a>
    </div>
  {/if}

  {#if showMesh}
    <MeshViewer {mesh} />
  {/if}
</div>
