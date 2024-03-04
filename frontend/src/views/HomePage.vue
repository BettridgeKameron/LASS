<template>
  <div id="app">
    <TitleComponent title="Lass-Home Page"></TitleComponent>
  </div>
  <div class="p-8">
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold mb-2">Linguistic Analysis & Stylometry Suite</h1>
      <p class="text-xl">
        CS 426 Senior Project in Computer Science, Spring 2024, at UNR, CSE Department
      </p>
    </div>

    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-4">Project Description</h2>
      <p class="text-lg">
        The Linguistic Analysis & Stylometry Suite, also known as LASS, is a set of tools designed
        around the concept of author attribution and
        <a
          class="link link-info"
          role="link"
          aria-label="Learn more about stylometry on Wikipedia"
          target="_blank"
          href="https://en.wikipedia.org/wiki/Stylometry"
        >
          stylometry.</a
        >
        In a world where it is becoming increasingly easier for threat actors to stay anonymous
        online, this project has the main goal of helping to identify threat actors based on their
        writing style, and to also provide some tools that will help with anonymity, due to there
        being legitimate reasons to be anonymous (such as whistle blowing). <br /><br />
        While the idea of using a piece of writing to de-anonymize threat actors is not new, as
        shown with the field of
        <a
          class="link link-info"
          role="link"
          aria-label="Learn more about forensic linguistics on Wikipedia"
          target="_blank"
          href="https://en.wikipedia.org/wiki/Forensic_linguistics"
        >
          forensic linguistics,</a
        >
        we hope that this tool will help advanced this field, as well as being something that is
        open source and accessible to anyone. There are also other uses and tools in this project
        such as predicting that someone is an author of a text in general based on past writings, or
        a tool that will rephrase text to appear to be styled by another person. <br /><br />
        Currently this project is being developed as a web app, with the potential for the back end
        to become publicly available to use. There are also plans to create a desktop version of the
        web app, where both the front end and back end can be used locally.
      </p>
    </div>

    <!-- There may be a component to replace the next div entirely, as we use it again for professors. If not this is a good thing to make into a component!-->
    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-4">Team Information</h2>
      <p class="text-lg mb-2">Team 18, LASS (Formerly CSFA)</p>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Team members loop -->
        <div v-for="member in teamMembers" :key="member.name" class="relative">
          <PersonCard
            :photo="member.photo"
            :name="member.name"
            :infoUrl="member.infoUrl"
            :description="`${member.major} Major`"
          />
        </div>
      </div>
    </div>

    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-4">Instructors & External Advisors</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Professor loop -->
        <div v-for="professor in professors" :key="professor.name" class="relative">
          <PersonCard
            :photo="professor.photo"
            :name="professor.name"
            :infoUrl="professor.infoUrl"
            :description="professor.role"
          />
        </div>
      </div>
    </div>

    <div>
      <h2 class="text-3xl font-bold mb-4">Project Related Resources</h2>
      <ul class="list-disc list-inside">
        <li>Problem domain book:</li>
        <ul class="list-disc list-inside ml-4">
          <li>
            <a
              class="link link-info"
              role="link"
              aria-label="Learn more about The Routledge Handbook of Forensic Linguistics"
              target="_blank"
              href="https://www.routledge.com/The-Routledge-Handbook-of-Forensic-Linguistics/Coulthard-May-Sousa-Silva/p/book/9780367531225"
              >The Routledge Handbook of Forensic Linguistics</a
            >
          </li>
        </ul>
        <br />
        <li>Related Websites/Tools:</li>
        <ul class="list-disc list-inside ml-4">
          <li>
            <a
              class="link link-info"
              role="link"
              aria-label="Learn more about Stylometry from Whonix"
              target="_blank"
              href="https://www.whonix.org/wiki/Stylometry"
              >Whonix Wiki page on stylometry</a
            >
          </li>
          <li>
            <a
              class="link link-info"
              role="link"
              aria-label="Learn more about the Java Graphical Authorship Attribution Program"
              target="_blank"
              href="http://evllabs.github.io/JGAAP/"
              >Java Graphical Authorship Attribution Program</a
            >
          </li>
          <li>
            <a
              class="link link-info"
              role="link"
              aria-label="Learn more about Anonymouth"
              target="_blank"
              href="https://github.com/psal/anonymouth"
              >Anonymouth</a
            >
          </li>
        </ul>
        <br />
        <li>Reference Articles</li>
        <ul class="list-disc list-inside ml-4">
          <li class="italic">
            Brennan, M., Afroz, S., Greenstadt, R.: Adversarial stylometry: circumventing authorship
            recognition to preserve privacy and anonymity. ACM Trans. Inf. Syst. Secur. (TISSEC)
            15(3), 1–22 (2012)
          </li>
          <li class="italic">
            Eder M, Rybicki J, Kestemont M. Stylometry with R: a package for computational text
            analysis. RJ. (2016) 8:15. doi: 10.32614/RJ-2016-007
          </li>
          <li class="italic">
            Ahmed Abbasi and Hsinchun Chen. 2008. Writeprints: A stylometric approach to
            identity-level identification and similarity detection in cyberspace. ACM Trans. Inf.
            Syst. 26, 2, Article 7 (March 2008), 29 pages.
            <a
              class="link"
              role="link"
              aria-label="Learn more about Writeprints"
              target="_blank"
              href="https://doi.org/10.1145/1344411.1344413"
              >https://doi.org/10.1145/1344411.1344413</a
            >
          </li>
          <li class="italic">
            Gomez Adorno, Helena & Rios, Germán & Posadas Durán, Juan & Sidorov, Grigori & Sierra,
            Gerardo. (2018). Stylometry-based Approach for Detecting Writing Style Changes in
            Literary Texts. Computación y Sistemas. 22. 10.13053/cys-22-1-2882.
          </li>
        </ul>
        <br />
        <li>Current Tech Stack</li>
        <ul class="list-disc list-inside ml-4">
          <li>Front End</li>
          <ul class="list-disc list-inside ml-4">
            <li>Vue.js</li>
            <li>Tailwind CSS</li>
            <li>daisyUI</li>
            <li>TypeScript</li>
          </ul>
          <li>Back End</li>
          <ul class="list-disc list-inside ml-4">
            <li>Flask</li>
            <li>Python</li>
          </ul>
        </ul>
      </ul>
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import PersonCard from '@/components/PersonCard.vue'
import TitleComponent from '@/components/TitleComponent.vue'

export default defineComponent({
  name: 'HomePage',
  components: {
    PersonCard,
  },
  data() {
    return {

      teamMembers: [
        {
          name: 'Kameron Bettridge',
          major: 'CSE',
          photo: '/img/kameron.jpg',
          infoUrl: 'https://linkedin.com/in/kbettridge'
        },
        {
          name: 'Alvin Leung',
          major: 'CSE',
          photo: '/img/alvin.jpg',
          infoUrl: 'https://linkedin.com/in/leungalvin2024'
        },
        {
          name: 'Raymond Pai',
          major: 'CSE',
          photo: '/img/raymond.jpg',
          infoUrl: 'https://www.linkedin.com/in/raymond-pai-0437a2270'
        },
        {
          name: 'Zachary Wilhite',
          major: 'CSE and Psychology',
          photo: '/img/zach.jpg',
          infoUrl: 'https://www.linkedin.com/in/zewilhite/'
        }
      ],
      professors: [
        {
          name: 'David Feil-Seifer',
          role: 'Instructor',
          photo: '/img/david.jpg',
          infoUrl: 'https://www.unr.edu/cse/people/david-feil-seifer'
        },
        {
          name: 'Devrin Lee',
          role: 'Instructor',
          photo: '/img/devrin.jpg',
          infoUrl: 'https://www.linkedin.com/in/devrinlee'
        },
        {
          name: 'Sara Davis',
          role: 'Instructor',
          photo: '/img/sara.jpg',
          infoUrl: 'https://www.unr.edu/cse/people/sara-davis'
        },
        {
          name: 'Emily Hand',
          role: 'Advisor',
          photo: '/img/emily.jpg',
          infoUrl: 'https://www.unr.edu/cse/people/emily-hand'
        }
      ]
    }
  }
})
</script>

<style scoped></style>
