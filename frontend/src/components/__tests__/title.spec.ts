// title.test.js
import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest'
import TitleComponent from '../TitleComponent.vue';

describe('TitleComponent.vue', () => {
  it('renders the correct title', () => {
    const title: string = 'This is a Title';
    const wrapper = mount(TitleComponent, {
      props: { title },
    });

    const h1 = wrapper.get('h1');
    expect(h1.text()).toBe(title);
  });
});