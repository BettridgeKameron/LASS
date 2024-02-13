import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import PersonCard from '@/components/PersonCard.vue'

describe('PersonCard', () => {
  it('contains name, infoUrl, and description in the DOM', () => {
    const wrapper = mount(PersonCard, {
      props: {
        photo: 'https://example.com/photo.jpg',
        name: 'John Doe',
        infoUrl: 'https://example.com/profile',
        description: 'Software Engineer'
      }
    })

    const link = wrapper.find('a')
    expect(link.exists()).toBe(true)
    expect(link.text()).toBe('John Doe')
    expect(link.attributes('href')).toBe('https://example.com/profile')

    const description = wrapper.find('p')
    expect(description.exists()).toBe(true)
    expect(description.text()).toBe('Software Engineer')
  })
})
