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
  {role}
  color={iconColor}
  ><path
    d="M3 13C6.6 5 17.4 5 21 13"
    stroke={iconColor}
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  ></path><path
    d="M12 17C10.3431 17 9 15.6569 9 14C9 12.3431 10.3431 11 12 11C13.6569 11 15 12.3431 15 14C15 15.6569 13.6569 17 12 17Z"
    stroke={iconColor}
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  ></path></svg
>
