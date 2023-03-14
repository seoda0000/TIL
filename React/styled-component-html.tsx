import styled from "styled-components";

export const STabItem = styled.div<any>`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 32px;
  font-size: 12px;
  background-color: ${(props) =>
    props.isValue ? "#ffffff" : "rgba( 255, 255, 255, 0 )"};
  color: ${(props) => (props.isValue ? "#000000" : "#612FAB")};
  border-radius: 4px;
`;
