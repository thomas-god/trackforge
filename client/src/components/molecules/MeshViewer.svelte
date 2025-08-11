<script lang="ts">
  import { onMount } from 'svelte';
  import { addToScene, createScene } from '$lib/scene';

  let { mesh }: { mesh: ArrayBuffer | undefined } = $props();

  let el: HTMLCanvasElement;

  $effect(() => {
    addToScene(mesh);
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
