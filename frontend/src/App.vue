<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start border-2 border-gray-300 p-2 rounded-md">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>

          <!-- This div is for thin screens -->
        </div>
        <ul
          tabindex="0"
          class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
        >
          <li><router-link to="/sentiment-analysis">Sentiment Analysis</router-link></li>
          <li><router-link to="/text-rephrase">Text Rephrase</router-link></li>
          <li><router-link to="/string-input">String Input</router-link></li>
          <li><router-link to="/fingerprint-creation">Fingerprint Creation</router-link></li>
        </ul>
      </div>

      <router-link class="btn btn-ghost text-xl" to="/">LASS</router-link>

      <!-- This div is for wider screens -->
      <div class="hidden lg:flex">
        <ul class="menu menu-horizontal px-1">
          <li><router-link to="/sentiment-analysis">Sentiment Analysis</router-link></li>
          <li><router-link to="/text-rephrase">Text Rephrase</router-link></li>
          <li><router-link to="/string-input">String Input</router-link></li>
          <li><router-link to="/fingerprint-creation">Fingerprint Creation</router-link></li>
        </ul>
      </div>
    </div>
    <!-- This is the toggle for dark and light -->
    <label class="navbar-end cursor-pointer grid place-items-center">
      <input
        type="checkbox"
        value="light"
        class="toggle theme-controller bg-base-content row-start-1 col-start-1 col-span-2"
      />
      <svg
        class="col-start-1 row-start-1 stroke-base-100 fill-base-100"
        xmlns="http://www.w3.org/2000/svg"
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
      </svg>
      <svg
        class="col-start-2 row-start-1 stroke-base-100 fill-base-100"
        xmlns="http://www.w3.org/2000/svg"
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <circle cx="12" cy="12" r="5" />
        <path
          d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"
        />
      </svg>
    </label>
  </div>
  <div id="content">
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'App'
})
</script>
