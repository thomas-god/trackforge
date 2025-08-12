<script lang="ts">
  import type { Props } from './types';

  let { size = 24, role = 'img', color, title }: Props = $props();

  let iconColor = $derived.by(() => {
    if (color === undefined) {
      const styles = getComputedStyle(document.documentElement);
      return styles.getPropertyValue('--color-base-content');
    }
    return color;
  });
</script>

<svg
  width={size}
  height={size}
  stroke-width="1.5"
  viewBox={`0 0 ${size} ${size}`}
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  aria-label={title}
  color={iconColor}
  {role}
  ><path
    d="M6 20L18 20"
    stroke={iconColor}
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  ></path><path
    d="M12 4V16M12 16L15.5 12.5M12 16L8.5 12.5"
    stroke={iconColor}
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  ></path></svg
>
