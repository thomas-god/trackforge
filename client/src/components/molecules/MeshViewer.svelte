<script lang="ts">
  import { onMount } from 'svelte';
  import { addToScene, createScene } from '$lib/scene';
  import type { Mesh } from '../../routes/+page.svelte';

  let { mesh }: { mesh: Mesh | undefined } = $props();

  let el: HTMLCanvasElement;

  $effect(() => {
    if (mesh === undefined) {
      return;
    }
    mesh.data.arrayBuffer().then((data) => {
      addToScene(data);
    });
  });

  onMount(() => {
    createScene(el);
  });
</script>

<svelte:head>
  <title>Three.js Sveltekit</title>
  <meta name="description" content="Three.js example app built with Svelte" />
</svelte:head>

<canvas bind:this={el}></canvas>
