import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";
import { WebView } from "react-native-webview";
import { Canvas, useFrame, useLoader } from "@react-three/fiber";
import * as THREE from "three";
import { useState, useRef, Suspense } from "react";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import test22 from "./assets/test/test22.gltf";

function Box(props) {
  const [active, setActive] = useState(false);

  const mesh = useRef();

  useFrame((state, delta) => {
    if (active) {
      mesh.current.rotation.x += delta;
      mesh.current.rotation.y += delta;
    }
  });

  return (
    <mesh
      {...props}
      ref={mesh}
      scale={active ? 1.5 : 1}
      onClick={(event) => setActive(!active)}
    >
      <boxGeometry />
      <meshStandardMaterial color={active ? "green" : "gray"} />
    </mesh>
  );
}

const Tree = () => {
  const gltf = useLoader(GLTFLoader, test22);

  return (
    <mesh>
      {/* <primitive object={gltf.scene} scale={10} />;<boxGeometry /> */}
    </mesh>
  );
};
export default function App() {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      {/* <Box /> */}
      {/* <Box position={[0, 2, 0]} /> */}
      {/* <Tree /> */}
      <Suspense fallback={<Box />}>
        <Tree />
      </Suspense>

      <mesh position={[-1, -3, 0]} scale={0.1}>
        <torusKnotGeometry radius={10} args={[10, 1, 260, 6, 10, 16]} />
        <meshStandardMaterial color={"green"} />
      </mesh>
    </Canvas>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
