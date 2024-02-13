<template>
  <div>
    <img :src="photo" :alt="`Photo of ${name}`" class="w-full h-auto" />
    <div
      class="absolute inset-0 bg-neutral bg-opacity-0 hover:bg-opacity-50 flex justify-center items-center opacity-0 hover:opacity-100 transition-opacity duration-300 ease-in-out"
    >
      <div class="text-center font-bold text-neutral-content">
        <a
          class="text-3xl link font-underline"
          role="link"
          :aria-label="`Learn more about ${name}`"
          target="_blank"
          :href="infoUrl"
          >{{ name }}</a
        >
        <p class="text-2xl">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonCard',
  props: {
    photo: String,
    name: String,
    infoUrl: String,
    description: String
  }
}
</script>

<style scoped></style>
