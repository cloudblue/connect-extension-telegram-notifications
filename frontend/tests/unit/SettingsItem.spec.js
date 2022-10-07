import { mount } from "@vue/test-utils";
import SettingsItem from "../../src/components/SettingsItem";

describe("SettingsItem", () => {
  it("shows 'Saving...' label if prop 'loading' is true", () => {
    const wrapper = mount(SettingsItem, {
      propsData: {
        loading: true,
      },
    });

    const loaderText = wrapper.get('[data-test="loader"]');

    expect(loaderText.text()).toBe('Saving...');
  });
});